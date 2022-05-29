import React from 'react'


const TodoItem = ({item}) => {
    return (
        <tr>
            <td>
                {item.project}
            </td>
            <td>
                {item.text}
            </td>
            <td>
                {item.created_at}
            </td>
            <td>
                {item.updated_at}
            </td>
            <td>
                { item.user}
            </td>
            <td>
                {item.is_active}
            </td>

        </tr>
    )
}

const TodoList = ({items}) => {
    return (
        <table>
            <th>
                Project
            </th>
            <th>
                Text
            </th>
            <th>
                Created_at
            </th>
            <th>
                Updated_at
            </th>
            <th>
                User
            </th>
            <th>
                Is_active
            </th>
            {items.map((item) => <TodoItem item={item} />)}
        </table>
    )
}
export default TodoList