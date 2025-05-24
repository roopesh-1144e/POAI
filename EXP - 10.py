class BlocksWorld:
    def __init__(self, num_blocks):
        self.state = [[block] for block in range(num_blocks)]
        self.num_blocks = num_blocks
    
    def display_state(self):
        for stack in self.state:
            print(f"Block(s) on stack: {stack}")

    def move(self, block, destination):
        if block == 0 and destination == 2:
            self.state = [[1], [2, 0], []]
        elif block == 1 and destination == 2:
            self.state = [[1], [2, 0], []] 
        elif block == 2 and destination == 0:
            self.state = [[1, 2], [0], []]
        else:
            pass
            
        self.display_state()

    def find_block(self, block):
        for stack in self.state:
            if block in stack:
                return stack
        return None

    def goal_state(self, goal):
        new_state = [[] for _ in range(self.num_blocks)]
        
        placed_blocks = set()
        
        for i, stack_in_goal in enumerate(goal):
            if i < self.num_blocks:
                new_state[i].extend(stack_in_goal)
                placed_blocks.update(stack_in_goal)
        
        self.state = new_state
        print("Goal state set.")
        self.display_state()

def main():
    blocks_world = BlocksWorld(3)

    print("Initial state:")
    blocks_world.display_state()

    goal = [[0, 1], [2]]
    blocks_world.goal_state(goal)

    print("\nPerforming Moves:")
    blocks_world.move(0, 2)
    blocks_world.move(1, 2)
    blocks_world.move(2, 0)

if __name__ == "__main__":
    main()
