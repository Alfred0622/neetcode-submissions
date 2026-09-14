class DynamicArray {
private:
    int capacity;
    int length;
    int *lst;
public:

    DynamicArray(int capacity) {
        
        this -> capacity = capacity;
        this -> length = 0;
        this -> lst = new int[capacity];
        
    }

    int get(int i) {
        if (i < capacity){
            return lst[i];
        }
    }

    void set(int i, int n) {
        if (i < capacity){
            lst[i] = n;
        }
    }

    void pushback(int n) {
        if (length == capacity){
            resize();
        }

        lst[length++] = n;
    }

    int popback() {
        int last_element;
        if (length > 0){
            last_element = lst[length - 1];
            length--;
        }

        return last_element;
    }

    void resize() {
        capacity *= 2;
        int* newlst = new int [capacity];
        for (int i = 0; i < length; i ++){
            newlst[i] = lst[i];
        }

        delete[] lst;
        lst = newlst;
        
    }

    int getSize() {
        return length;
    }

    int getCapacity() {
        return capacity;
    }
};
