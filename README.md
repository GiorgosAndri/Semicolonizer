# Semicolonizer
#### Video Demo:  <https://www.youtube.com/watch?v=CklESSo0SrI>

#### Description:

#### This is the final project of the course Cs50 Introduction to Computer science. The project called Semicolonizer is a project that takes as an input C code and adds any semicolon missing in the final output. You can either use the algorithm.py for generating a C file or you can use the web application where you can copy the output.

#### First I created the algorithm.py. Here we have the algorithm that puts the semicolons in our code. It can also be used independently to generate the C file without having to use the website.

#### So how it works? In the beginning, we split the lines so that each line is an independent string. In addition, we declare the variables that we will need to use later and need to stay out of the for loop and we begin our for loop that loops each line of our initial code. In the beginning we put each line in a variable called line that strips them from the extra spaces so we can check what we want easier. Then we check for areas that either already have semicolons, or are library imports or comments. Then we check for bugs that can be generated due to the way python handles strings. Something that we will also do later. Then, we check in case there is a declaration of a function and we have finished the first part of checks. After all these checkings, we begin to check for the existence of each C function that we were taught at CS50 and some more that could be found in C documentation and we act accordingly to each function. After that, we check for possible bugs generated due to the way python handles strings and we fix them.In the end, we check for the values where we add semicolons and we add them. After that, we check for double semicolons that might be put and we clean our code further from "trash" that were generated due to debugging. After all that, we put everything together on the variable called updated. If we run the file algorithm.py and we add an input(in my case, I added the file code_sample.txt, which is my tideman algorithm desemicolonized), we will get as an output a C file, which will be our code "semicolonized" and we can run the "make" command and run the file for checking for any bugs. In the code_sample's case, everything is good.



#### Second, I created the index.html where I decided what design and features it will have. I set as background a gold semicolon and added two text areas. 1 for the input on the left and one for the output on the right. I then added the Semicolonize button above the input textarea and the copy button above the output text area.


#### Finally, after deciding which variables and buttons will be used, I created the flask application app.py, where user's input is processed through our algorithm and prints user's output where the user can copy it using the copy button.



### Author

Georgios Andrigiannakis

 email: andrigiannakhs94@gmail.com
[LinkedIn](https://www.linkedin.com/in/georgios-andrigiannakis-9890a018a/)
