 // SPDX-License-Identifier: MIT
pragma solidity ^0.8.12;

contract Student_management {
    struct Student {
        int stud_id;
        string name;
        string department;
    }
    Student[] Students;

    function add_stud(int stud_id, string memory name, string memory department) public {
        Students.push(Student(stud_id, name, department));
    }

    function getStudent(int stud_id) public view returns (string memory, string memory) {
        for (uint i = 0; i < Students.length; i++) {
            if (Students[i].stud_id == stud_id) {
                return (Students[i].name, Students[i].department);
            }
        }
        return ("Not Found", "Not Found");
    }

    receive() external payable {}
    fallback() external payable {}
}