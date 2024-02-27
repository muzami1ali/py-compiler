int exampleFunction(int a) {
    if (a < 0) {
        return -1; // First return statement
    } else if (a == 0) {
        return 0; // Second return statement
    } else {
        return 1; // Third return statement
    }
}

int main(){
   exampleFunction(10);
   return 0;
}
