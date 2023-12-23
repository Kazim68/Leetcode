#include <vector>
using namespace std;

class MinStack {
public:
    vector<int> min;
    vector<int> stack;
    MinStack() {
        min.push_back(INT_MAX);
    }
    
    void push(int val) {
        stack.push_back(val);
        if (val <= min.back()){
            min.push_back(val);
        }
    }
    
    void pop() {
        if (stack.back() == min.back()){
            min.pop_back();
        }
        stack.pop_back();
        
    }
    
    int top() {
        return stack.back();
    }
    
    int getMin() {
        return min.back();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */