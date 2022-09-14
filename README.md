# Visualizing Linear Transformations

1. **What we aim to do here**

Linear transfors are one of the core concepts in linear algebra. A large number of concepts in linear algebra can be understood with a great understanding of the linear transforms. Through this project, we aim to create a tool that would help in the visualization of linear algebra concepts through linear transformations in the 2D coordinate plane.

2. **Project design**

We aim to design a 2D cartesian plane with the help of pygame library. Features that we aim to give:

1. Creating a 2D plane :

<https://github.com/DeVcB13d/Linear-Transform-Visualisation/tree/main/media/pg1.jpg>


* The above shown picture is a model of the 2D plane that we aim to implement
* Critical features to be added
  * Basic coordinate plane with number markings and stuff
  * Getting back the coordinate in cartesian system and the vice versa.
  * Need to able to move the plane with keys and the number markings should change appropriately
  * To be able to zoom into the plane
  * Also the plane should be able to move properly
  * Add the linear transform change to the plane (blue lines)
* Creating an interactive interface using tkinter :
  1.Making two frames :To enter two vectors for transformation
   2.Creating two buttons:Run simulation and calculating transformed vector.
  

2. Adding linear algebra features to the tool

* Once the linear tranformation part is clearly done and visualized the next step is to add some linear algebra functionalities
    1. Solving a linear equation : The solution to a linear equation AX = b is the coordinate of the point that would eventually reach b after the transform A
    2. Matrix multiplications and its applications : Matrix multiplication AXB is applying a transformation on the A on the standard plane and applying B on the new transformed plane.
    3. Null Space of a matrix : The vectors that go into 0 vector after the transformation A.
    4. Eigenvectors : These vectors would only get streched by a certain amount on applying the transformation, so we have to highlight the vectors that would only get streched
    5. Finding the determinant : change in area after transformation.

# **Design implementaion**

1. PHASE 1 : Designing the 2D plane:

**Desired Properties:**

* Need to be extremely generalized and be open for expansion
* Should be able to apply the linear algebra operations on the plane easily

**Ideas/Algorithms for design:**

1. Designing a mathematically accurate 2D plane with various features : 

* 



**Ideas to add Linear algebra functionalities**