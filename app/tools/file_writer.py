class FileWriterTool:
    def write_plan(self, content):
        with open("travel_plan.md", "w") as f:
            f.write(content)
        return "Plan saved to travel_plan.md"

file_writer = FileWriterTool()