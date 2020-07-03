# Generating Code for Enums

Wabbit has enum definitions like this:

```
enum MaybeInt {
    Nope;
    Some(int);
};

// Example of how to create values
var x = MaybeInt::Nope;
var y = MaybeInt::Some(42);

// Example of matching
func f(a MaybeInt) int {
    return match a {
         Nope => -1;
         Some(z) => 100*z;
    };
}

print f(x);   // Prints -1
print f(y);   // Prints 4200
```

Implementing enums is perhaps the most difficult part of the project.  This page will give you a hint.

## Enums as Tagged Structs

One way to implement an enum is as a struct with a type-tag.  For example, the above enum definition could be turned into a struct:

```
struct MaybeIntStruct {
     tag int;
     Some int;
};

var x = MaybeIntStruct(0, 0);    // Tag 0 == Nope
var y = MaybeIntStruct(1, 42);   // Tag 1 == Some(42)

func f(a MaybeIntStruct) int {
    var result int;
    if a.tag == 0 {
        result = -1;
    }
    if a.tag == 1 {
        var z = a.Some;
        result = 100*z;
    }
    return result;
}
```

## Implementation Strategy

To make enums work, it makes sense to build upon your structure code.  However, you might be able to do it in different places.  For example, it might be possible to implement enums entirely within high-level Wabbit code by performing some sort of syntactic transformation or generating support code behind the scenes.  You could also choose to do it at a lower-level such as LLVM--building heavily upon your implementation of structs.
