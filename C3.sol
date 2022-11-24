//SPDX-License-Identifier: MIT
pragma solidity >=0.5.0 <0.9.0;

contract StudentMgmt {
    struct Student {
        int256 stud_id;
        string name;
        string department;
    }
    Student[] StudentsList;

    function addStudent(
        int256 stud_id,
        string memory name,
        string memory department
    ) public {
        Student memory stud = Student(stud_id, name, department);
        StudentsList.push(stud);
    }

    function getStudent(int256 stud_id)
        public
        view
        returns (string memory, string memory)
    {
        for (uint256 i = 0; i < StudentsList.length; i++) {
            Student memory stud = StudentsList[i];
            if (stud.stud_id == stud_id) {
                return (stud.name, stud.department);
            }
        }
        return ("Not Found", "Not Found");
    }

    fallback() external {
        x = x + 1;
    }

    uint256 x;
}
