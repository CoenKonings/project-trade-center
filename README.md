# Project Trade Center
A web-based application that helps students at HKU find someone to trade their assigned projects with.
The system creates a directed graph, where each node represents a project and each proposal is represented by an edge. When a new proposal is made, the system checks for cycles in the graph. If a cycle is created by the new proposal, the people whose proposals are part of the cycle are matched and instructed to contact the teacher to trade projects.
