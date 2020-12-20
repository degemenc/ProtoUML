# ProtoUML

This is a snippet of python script that you can use to convert your proto files to UML diagrams in under a minute. This script converts your proto file to a java file, and you can use it to generate UML from java source code in IntelliJ IDEA.

Do not worry about the int32, bool etc. data types of proto syntax, even though IntelliJ shows errors in the code, it doesn't care about them while creating UMLs.

**Notice:** the java file generated with this tool is not a compiled proto file! It is a mock java file, useful only for UML creation.

You can help by creating pull requests if you make improvements.

## Pre-Requisites
- Python 3
- JetBrains IntelliJ IDEA Ultimate (if you don't have Ultimate version, look at [ObjectAid plugin](https://www.objectaid.com/home) for Eclipse IDE to serve the same purpose)

## How?
1. Download the protoToJavaForUML.py file
2. Run it on your console with ```python3 protoToJavaForUML.py [YOUR_PROTO_FILE] [NAME_OF_THE_OUTPUT_FILE_YOU_WANT]```
    - Example: ```python3 protoToJavaForUML.py myProject.proto myProject.java```
3. Do the steps at [IntelliJ UML generation](https://www.jetbrains.com/help/idea/class-diagram.html#analyze_class) or use ObjectAid plugin for Eclipse
    - Example: Open a new project in IntelliJ, put ```myProject.java``` in 'src' folder. Right click on 'src' -> Diagrams -> Show Diagram. Customize your diagram from the top bar, explained in the link given above.