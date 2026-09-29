# pygame-physics-tutorial
This repository teaches how to handle physics, collisions and character controlling in Pygame step by step, starting from the very basics and building up new concepts each iteration.

Each chapter is written in understandable Python with comments explaining concepts and sections. They are meant to be self-explanatory, without any supplemantel blogs/articles or documentation.

The only preqrequisite is that, you should have a grasp of pygame itself, even if you're a beginner. Because this tutorial focuses on explaining higher level concepts rather than the pygame library itself.

Feel free to change, edit and experiment with chapters source code to understand better!



# Chapters
- [**Chapter 0 - Movement**](chapters/0_movement.py): This chapter is about introducing vector arithmetic, using `pygame.Vector2`s and basic WASD movement.



# Installation & Running
### 📌 Prerequisites
- [Python 3.12+](https://www.python.org/downloads/)

**1.** Clone the repository.
```shell
$ git clone https://github.com/kadir014/pygame-physics-tutorial.git
$ cd pygame-physics-tutorial
```
**2..** Install [pygame-ce](https://github.com/pygame-community/pygame-ce), which is the only dependency. (Also remove the upstream pygame if it was installed before, as it's not maintained anymore.)
```shell
$ python -m pip uninstall pygame
$ python -m pip install pygame-ce
```

**3.** Run any chapter you'd like.
```shell
$ python chapters/0_vectors.py
```



# License
[MIT](LICENSE) © Kadir Aksoy