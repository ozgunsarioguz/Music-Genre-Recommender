print("\n This program is a basic recommendation robot recommending a music type depending on user input! \n So let's get started.\n \n ")

# This program is a basic recommendation robot which returns a user music type(s) according to their selection, depending on several categories.
# These categories are: Mood, Speed
# 
# classical(slow), blues-country (upbeat-slow), edm-techno (upbeat), deep-house(slow), jazz(upbeat-slow), latin(upbeat), metal(upbeat), pop(upbeat), rnb(upbeat), rock (slow-upbeat)

# TREENODE CLASS

music_types = ["classical", "blues-country", "edm-techno", "deep-house", "jazz", "latin", "metal", "pop", "rnb", "rock"]

music = ["Music", "Please select your music type selection 1: Slow or 2: Upbeat.\n"]
slow = ["Slow", "Please select your slow music type selection 1: Ethnic/Classics or 2: Modern.\n"]
upbeat = ["Upbeat", "Please select your upbeat music type selection 1: Ethnic/Classics or 2: Modern.\n"]
slow_old = ["slow_old", ["classical", "blues-country"]]
slow_modern = ["slow_modern", ["deep-house", "jazz", "rock-ballad"]]
upbeat_old = ["upbeat_old", ["blues-country", "latin"]]
upbeat_modern = ["upbeat_modern", ["edm-techno", "jazz", "metal", "pop", "rnb", "rock"]]



class TreeNode:
  def __init__(self, music):
    self.music = music
    self.choices = []

  def add_child(self, node):
    self.choices.append(node)

  def traverse(self):
    story_node = self
    while len(story_node.choices) > 0:
      print(story_node.music[1])
      user_choice = input("Select and write 1 or 2 ... ")
      if user_choice == "1" or user_choice == "2":
        user_choice = int(user_choice)
        chosen_child = story_node.choices[user_choice - 1]
        story_node = chosen_child
      else:
        print("Please write 1 or 2 your input was not clear...")
    print("You may listen to: \n ")
    for i in story_node.music[1]:
        print(f"{i} \n")
    print("\n Thanks for using genre recommender.\n")



story_root = TreeNode(music)

choice_slow = TreeNode(slow)

choice_upbeat = TreeNode(upbeat)

choice_slow_old = TreeNode(slow_old)

choice_slow_act = TreeNode(slow_modern)

choice_upbeat_old = TreeNode(upbeat_old)

choice_upbeat_act = TreeNode(upbeat_modern)

story_root.add_child(choice_slow)
story_root.add_child(choice_upbeat)
choice_slow.add_child(choice_slow_old)
choice_slow.add_child(choice_slow_act)
choice_upbeat.add_child(choice_upbeat_old)
choice_upbeat.add_child(choice_upbeat_act)


story_root.traverse()


