# EC463 - Senior Design - MiniProject Report - Yagiz Idilman and Peter West 

## Exercise 1 Answer and Explanation 

1 - What are the "max_bright" and "min_bright" values you found?

- max_bright = 29000  
- min_bright = 8000  

We've conducted our light experiment in the Engineering Library on campus. So the values would change depending on the environment you are in. The following images show the recorded values for max_bright and min_bright on our console:

- [Exercise 1 - Light Data (1)](https://github.com/f-libble/2024-mini/blob/main/assignment/Exercise%201%20-%20Video%20%26%20Screenshots/Exercise%201%20-%20Late%20Data%20(1).PNG)  
- [Exercise 1 - Light Data (2)](https://github.com/f-libble/2024-mini/blob/main/assignment/Exercise%201%20-%20Video%20%26%20Screenshots/Exercise%201%20-%20Late%20Data%20(2).PNG)  

The following video demonstration shows that with our max_bright and min_bright values, the light on the Pi Pico board goes ON when the photosensor determines that the room is dim or dark, and the light on the board goes OFF when the environment gets bright. Watch the video here:

- [Exercise 1 - Demo.mp4](https://github.com/f-libble/2024-mini/blob/main/assignment/Exercise%201%20-%20Demo.mp4)


## Exercise 2 Answer and Explanation 

Modifying the `exercise_sound.py`, it now generates sound using PWM (Pulse Width Modulation) on a speaker to play the main melody of the Super Mario Bros theme. The melody is represented by a list of frequencies, and each note is played for a specific duration using a loop. The following video demonstrates the Super Mario Bros theme song playing:

- [Exercise 2 - Demo.mov](https://github.com/f-libble/2024-mini/blob/main/assignment/Exercise%202%20-%20Demo%20.mov)


## Exercise 3 Answer and Explanation 

Exercise 3 consists of 2 parts, `exercise_game.py` and `exercise_login.py`. For `exercise_game.py` we needed to modify the existing code to be able to communicate with a realtime Firebase database. As the code sends the data to the Firebase database, it uses a user ID to specify in the URL to the realtime database that the data being sent should fall under a certain user. Next, in `exercise_login.py` we need to specify how we (r)egister, (l)ogin, and (v)iew a certain user specified by their email (Note: you can see the user's email in the view option).

- [Exercise 3 - Demo](https://github.com/f-libble/2024-mini/tree/84d8c81bc4b57a3a5c471a9ada92a8d4c1cc0725/assignment/Exercise%203%20-%20Video%20%26%20Screenshots)