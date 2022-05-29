import React from 'react'


const ProjectItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.id}
            </td>
            <td>
                {item.name}
            </td>
            <td>
                {item.repo_link}
            </td>
            <td>
                {item.user.id}
            </td>
        </tr>
    )
}

const ProjectList = ({items}) => {
    return (
        <table>
            <th>
                ID
            </th>
            <th>
                Name
            </th>
            <th>
                Repo_link
            </th>
            <th>
                User
            </th>
            {items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}
export default ProjectList