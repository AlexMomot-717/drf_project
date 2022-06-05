import React from 'react'
import { useParams } from 'react-router-dom'


const ProjectItem = ({item}) => {
    return (
        <tr>
            <th>
                { item.id }
            </th>
            <td>
                { item.name }
            </td>
            <td>
                { item.repo_link }
            </td>
            <td>
                { item.user.id }
            </td>
        </tr>
    )
}

const UserProjectList = ({ items }) => {
    let { id } = useParams();
    let filtered_items = items.filter((item) => item.user.id == id)
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
            {filtered_items.map((item) => <ProjectItem item={item} />)}
        </table>
    )
}
export default UserProjectList