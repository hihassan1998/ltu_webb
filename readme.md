# Hassans Python Projects
This repository contains multiple Python-based projects, including:

**Yahtzee Game** 🎲: An object-oriented implementation of the classic dice game.

**8 Fingers 2 Thumbs Typing Test** ⌨️: A CLI-based typing game to improve typing speed and accuracy.

**Binary Search Tree Implementation**  🌳🍃: Implementation of a flexible Binary Search Tree (BST)

## 📌 Projects
### 🎲 Yahtzee Game (Located in yahtzee/)

An **object-oriented Python project** that simulates the Yahtzee game using structured code and design patterns. The goal is to implement game mechanics efficiently while practicing **OOP principles, class management, and algorithm design.

#### 🔍 Features:

- Full Yahtzee rules implementation
- Object-oriented structure with clear class separation
- Flask-based web interface for gameplay
- Score tracking

#### 🛠️ Tech Stack:

Python 🐍
Flask 🌍
Bootstrap 🎨
Vanilla CSS 🎭

####  Visual Overview

### ⌨️ 8 Fingers 2 Thumbs - Typing Test (Located in typing/)
A **command-line typing test game** designed to enhance typing speed and accuracy. Players can compete against themselves in three difficulty levels (Easy, Medium, Hard) while tracking their results.

#### 🔍 Features:
- Interactive CLI interface
- Three difficulty levels
- Real-time score tracking and saved results
- Built-in error handling for missing or improperly formatted files

#### 🛠️ Tech Stack:
Python 🐍
File Handling 📂
Exception Management ⚠️
Text Processing 📝

####  Visual Overview

![82](https://github.com/user-attachments/assets/b5d66a05-5992-4813-b08d-c044a052e408)

### Binary Search Tree (Located in binarySearchTree/)
This project contains the implementation of a flexible Binary Search Tree **(BST)**, with two primary classes: Node and BinarySearchTree.

#### Node Class
The Node class represents a single node in the binary search tree. It holds the following properties:

- key: The unique identifier for the node.
- value: The value associated with the key.
- left: A reference to the left child node.
- right: A reference to the right child node.
- parent: A reference to the parent node.

The Node class provides several utility methods to:

- Check if the node is a leaf, has children, or has both children.
- Compare nodes based on their keys.
#### BinarySearchTree Class
The BinarySearchTree class manages the overall tree structure and operations. It includes methods to:

- Insert nodes while maintaining the binary search property.
- Remove nodes by handling various cases, such as leaf nodes, nodes with one child, and nodes with two children.
- Get the value associated with a key by performing a search.
- Traverse the tree using an inorder traversal, printing node values in sorted order.
- Get size of the tree (total number of nodes).

These classes provide a simple, efficient implementation of a binary search tree with recursive methods for insertion, removal, and search.
