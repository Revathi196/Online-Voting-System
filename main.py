# main.py

class VotingSystem:
    def __init__(self):
        self.candidates = {}
        self.votes = {}

    def add_candidate(self, name):
        """Add a new candidate."""
        if name not in self.candidates:
            self.candidates[name] = 0
            print(f"Candidate '{name}' has been added.")
        else:
            print(f"Candidate '{name}' already exists.")

    def show_candidates(self):
        """Display available candidates."""
        print("\nAvailable Candidates:")
        for idx, candidate in enumerate(self.candidates, start=1):
            print(f"{idx}. {candidate}")

    def cast_vote(self, voter_id, candidate_name):
        """Allow a user to cast a vote."""
        if candidate_name not in self.candidates:
            print(f"Candidate '{candidate_name}' not found.")
            return
        if voter_id in self.votes:
            print(f"Voter '{voter_id}' has already voted.")
            return
        self.votes[voter_id] = candidate_name
        self.candidates[candidate_name] += 1
        print(f"Vote cast successfully for '{candidate_name}'.")

    def show_results(self):
        """Display the voting results."""
        print("\nVoting Results:")
        for candidate, votes in self.candidates.items():
            print(f"{candidate}: {votes} votes")


def main():
    system = VotingSystem()
    
    # Add candidates
    while True:
        add_more = input("Do you want to add a new candidate? (yes/no): ").strip().lower()
        if add_more == "yes":
            candidate_name = input("Enter candidate name: ").strip()
            system.add_candidate(candidate_name)
        else:
            break

    # Voting process
    while True:
        system.show_candidates()
        voter_id = input("\nEnter your voter ID: ").strip()
        candidate_name = input("Enter the name of the candidate you want to vote for: ").strip()
        system.cast_vote(voter_id, candidate_name)
        
        more_voting = input("\nDo you want to vote again? (yes/no): ").strip().lower()
        if more_voting != "yes":
            break
    
    # Show results
    system.show_results()


if __name__ == "__main__":
    main()
