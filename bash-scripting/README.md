# Ram Hacks | Bash Scripting

## Topic Overview

- [Ram Hacks | Bash Scripting](#ram-hacks--bash-scripting)
  - [Topic Overview](#topic-overview)
  - [Introduction to Bash](#introduction-to-bash)
  - [Variables](#variables)
  - [Conditionals](#conditionals)
  - [Loops](#loops)
  - [Functions](#functions)
  - [Exercise](#exercise)

## Introduction to Bash

Welcome to the wonderful world of Bash scripting! But wait, what *is* Bash? Bash is a Unix shell and command language that is used to interact with the operating system. It is a powerful tool that can be used to automate tasks, write complex scripts, and more. In this workshop, we will cover the basics of Bash scripting, including variables, conditionals, loops, and functions. We will also touch on how to use Bash to automate tasks and write more complex scripts.

But wait - we've probably seen Bash before, right? If you've ever used the command line on a Unix-based system (like Linux or macOS), you've used Bash! It's the default shell for these systems, and it's a powerful tool for interacting with the operating system.

For example, maybe you've done something like this before:

```bash
$ ls
```

or

```bash
$ python3 my_script.py
```

These are both examples of using Bash to interact with the operating system. In the first example, we're using Bash to list the files in the current directory. In the second example, we're using Bash to run a Python script.

## Variables

Variables are a fundamental concept in programming, and Bash is no exception. In Bash, variables are used to store data that can be used later in the script. Variables can store all sorts of data, including strings, integers, and more.

To create a variable in Bash, we use the following syntax:

```bash
my_variable="Hello, world!"
```

Notice that we don't use spaces around the `=` symbol. This is because Bash treats spaces as delimiters, so if we included spaces around the `=` symbol, Bash would think we're trying to run a command called `my_variable` with the arguments `"Hello,"` and `"world!"`. That's not what we want!

In this example, we're creating a variable called `my_variable` and setting it equal to the string "Hello, world!". We can then use this variable later in the script, like so:

```bash
echo $my_variable
```

Keep in mind, when we want to access the value of a variable, we use the `$` symbol before the variable name. This tells Bash to replace the variable name with its value. If we forget the `$` symbol, Bash will treat the variable name as a string, rather than its value.

## Conditionals

Conditionals are used to make decisions in a script. They allow us to execute different code based on whether a condition is true or false. In Bash, we use the `if` statement to create conditionals.

The basic syntax for an `if` statement in Bash is as follows:

```bash
if [ condition ]; then
  # code to run if the condition is true
fi
```

In this example, `condition` is a test that can be evaluated as true or false. If `condition` is true, the code inside the `if` statement will be executed. If `condition` is false, the code inside the `if` statement will be skipped.

Like other languages, Bash has a variety of operators that can be used to create conditions. Here are a few examples:

- `-eq`: equal to
- `-ne`: not equal to
- `-lt`: less than
- `-le`: less than or equal to
- `-gt`: greater than
- `-ge`: greater than or equal to
- `=`: string equal to
- `!=`: string not equal to
- `-o`: logical OR
- `-a`: logical AND
- `!`: logical NOT

Here's an example of using an `if-else` statement in a Bash script:

```bash
#!/bin/bash

if [ $1 -eq 0 ]; then
  echo "The number is zero"
else
  echo "The number is not zero"
fi
```

In this example, we're using the `-eq` operator to test if the first command line argument is equal to zero. If it is, we print "The number is zero". If it's not, we print "The number is not zero".

## Loops

Loops are used to repeat a block of code multiple times. In Bash, we can use the `for` and `while` loops to create loops.

The basic syntax for a `for` loop in Bash is as follows:

```bash
for item in list; do
  # code to run for each item in the list
done
```

In this example, `list` is a list of items, and `item` is a variable that will be set to each item in the list in turn. The code inside the `for` loop will be executed once for each item in the list.

Here's an example of using a `for` loop in a Bash script:

```bash
#!/bin/bash

for i in 1 2 3 4 5; do
  echo $i
done
```

In this example, we're using a `for` loop to print the numbers 1 through 5.

The basic syntax for a `while` loop in Bash is as follows:

```bash
while [ condition ]; do
  # code to run while the condition is true
done
```

In this example, `condition` is a test that can be evaluated as true or false. The code inside the `while` loop will be executed repeatedly as long as `condition` is true.

Here's an example of using a `while` loop in a Bash script:

```bash
#!/bin/bash

i=0
while [ $i -lt 5 ]; do
  echo $i
  i=$((i+1))
done
```

In this example, we're using a `while` loop to print the numbers 0 through 4.

## Functions

Functions are used to group code together and give it a name. This allows us to reuse the code multiple times without having to copy and paste it. In Bash, we can use the `function` keyword to create functions.

The basic syntax for a function in Bash is as follows:

```bash
function my_function {
  # code to run when the function is called
}
```

In this example, `my_function` is the name of the function, and the code inside the function will be executed when the function is called.

Here's an example of using a function in a Bash script:

```bash
#!/bin/bash

function greet {
  echo "Hello, world!"
}

greet
```

In this example, we're using a function called `greet` to print "Hello, world!".

That's it for the basics of Bash scripting! We've covered variables, conditionals, loops, and functions. With these tools, you can start writing your own Bash scripts to automate tasks, write complex scripts, and more. Happy scripting!

## Exercise

Now that we've covered the basics of Bash scripting, it's time to put your knowledge to the test!

First, let's create a new Python file called `my_script.py` and write a simple Python script that sorts a list of numbers. Here's an example to get you started:

```python
#!/usr/bin/env python3

def sort_numbers(numbers):
  return sorted(numbers)

if __name__ == "__main__":
    numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_numbers = sort_numbers(numbers)
    print(sorted_numbers)
```

Next, let's create a new Bash script called `my_script.sh` that runs the Python script ``n`` times, where ``n`` is a command line argument. Here's an example to get you started:

```bash
#!/bin/bash

n=$1
for i in $(seq 1 $n); do
  python3 my_script.py
done
```

For your exercise, try modifying the Bash script above to time how long each run of the Python script takes, outputting the average time to a file called `average_time.txt`. You can use the `time` command to time how long a command takes, and the `>>` operator to append output to a file.

Good luck, and happy scripting!

<details> 
  <summary> Solution </summary>

```bash
#!/bin/bash

n=$1
total_time=0
for i in $(seq 1 $n); do
  (time -p python3 my_script.py) 2> time.txt
  time=$(grep real time.txt | awk '{print $2}')
  total_time=$(echo "$total_time + $time" | bc)
done
average_time=$(echo "scale=3; $total_time / $n" | bc)
echo $average_time >> average_time.txt
```

</details>