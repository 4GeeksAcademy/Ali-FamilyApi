"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint


class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        # example list of members
        self._members = [
           {'id': 10, 'name': 'John', 'last_name': self.last_name, 'age': '33', 'lucky_numbers': [7, 13, 22]},
           {'id': self._generate_id(), 'name': 'Jane', 'last_name': self.last_name, 'age': '35', 'lucky_numbers': [10, 14, 3]},
           {'id': self._generate_id(), 'name': 'Jimmy', 'last_name': self.last_name, 'age': '5', 'lucky_numbers': [1]}
        ]

    # Read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Fill this method and update the return
        member["last_name"] = self.last_name
        member['id']= self._generate_id()
        self._members.append(member)
        return self._members

    def delete_member(self, member_id):
        self._members = [row for row in self._members if row["id"] != member_id]
        return self._members

    def get_member(self, member_id):
        return [row for row in self._members if row["id"] == member_id]

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
