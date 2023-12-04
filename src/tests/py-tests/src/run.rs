use std::{fs::read_to_string, path::PathBuf, process::Command};

use lang_tester::LangTester;
use tempfile::TempDir;

static COMMENT_PREFIX: &str = "#";

fn main() {
    // We use compile.py to compile files into a binary: we store those binary files
    // into `tempdir`. This may not be necessary for other languages.
    let tempdir = TempDir::new().unwrap();
    LangTester::new()
        .test_dir("src/lang_tests")
        // Only use files named `*.py` as test files.
        .test_file_filter(|p| p.extension().unwrap().to_str().unwrap() == "py")
        // Extract the first sequence of commented line(s) as the tests.
        .test_extract(|p| {
            read_to_string(p)
                .unwrap()
                .lines()
                // Skip non-commented lines at the start of the file.
                .skip_while(|l| !l.starts_with(COMMENT_PREFIX))
                // Extract consecutive commented lines.
                .take_while(|l| l.starts_with(COMMENT_PREFIX))
                .map(|l| &l[COMMENT_PREFIX.len()..])
                .collect::<Vec<_>>()
                .join("\n")
        })
        // We have two test commands:
        //   * `Compiler`: runs python3 compile.py input output.
        //   * `Run-time`: if command does not error, and the `Compiler` tests
        //     succeed, then the output binary is run.
        .test_cmds(move |p| {
            // Test command 1: Compile `x.py` into `tempdir/x`.
            let mut exe = PathBuf::new();
            exe.push(&tempdir);
            exe.push(p.file_stem().unwrap());
            let mut compiler = Command::new("python3");
            compiler.args(&["src/compile.py",p.to_str().unwrap(), exe.to_str().unwrap()]);
            // Test command 2: run `tempdir/x`.
            let runtime = Command::new(exe);
            vec![("Compiler", compiler), ("Run-time", runtime)]
        })
        .run();
}