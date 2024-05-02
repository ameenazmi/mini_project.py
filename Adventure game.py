name = input("Your name: ").capitalize()
print(f"Welcome {name} to Adventure Game")

print(f"Today, {name} determined to embark on a grand adventure. With {name} knapsack packed and {name} heart brimming with excitement, {name} sets off into the unknown. As {name} wanders through the forest, {name} comes to a fork in the path. To {name} left, a narrow trail disappears into the dense thicket, while to {name} right, a winding path leads deeper into the heart of the woods.")
left_right = input("Which path should you go? (Left/ Right) ").lower()

if left_right == "left":
    cave_river = input("You have choose left path, now you need to choose to go through? (Cave/ River). ")

    if cave_river == "cave":
        print("You don't have torchlight and you got attacked by coronavirus bat")
        print("GAME OVER!")
    
    elif cave_river == "river":
        print("You struggle to swim and crocoadile have chase you")
        print("Badly, you didn't make it")
        print("GAME OVER!")

    else:
        print("invalid options. YOU DEAD!")

elif left_right == "right":
    treachous_steep = input("You need to choose treachous path or steep path (Treachous/ Steep). ").lower()

    if treachous_steep == "treachous":
        print("You make it!")
        print(f"{name} arrived at beautiful places!")
        print("Congratulations!")
    
    elif treachous_steep == "steep":
        print("You are not a skillful climber!")
        print("Now, you were stranded!")
        print("GAME OVER!")

    else:
        print("invalid options. YOU DEAD!")

else:
    print("What are you doing?")
    print("GAME OVER!")

