from .models import Project

def find_matches(proposal):
    queue = []
    visited = [proposal.to_project]
    target_node = proposal.from_project
    queue.append([proposal])

    while queue:
        path = queue.pop(0)
        current_node = path[-1].to_project

        if current_node == target_node:
            return path

        for edge in current_node.offers.filter(accepted=False):
            if edge.to_project.id not in visited:
                visited.append(edge.to_project.id)
                new_path = path.copy()
                new_path.append(edge)
                queue.append(new_path)

    return []
