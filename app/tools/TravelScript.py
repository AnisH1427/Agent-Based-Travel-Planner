class TravelPlanScribe:
    def write_plan(self, content):
        with open("travel_plan.md", "w", encoding="utf-8") as f:
            f.write(content)
        return "Plan saved to travel_plan.md"

plan_scribe = TravelPlanScribe()
