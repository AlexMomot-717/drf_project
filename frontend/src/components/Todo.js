import React from 'react'
import {Link} from 'react-router-dom'



const TodoItem = ({item, deleteTodo}) => {
    return (
        <tr>
            <td>
                {item.id}
            </td>
            <td>
                {item['project']}
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
                {item['user']}
            </td>
            <td>
                {item.is_active}
            </td>
            <td>
                <button onClick={()=>deleteTodo(item.id)} type='button'>Delete</button>
            </td>

        </tr>
    )
}

const TodoList = ({items, deleteTodo}) => {
    return (
        <div>
        <table>
            <tr>
                <th>
                    ID
                </th>
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
                <th></th>
            </tr>
            {items.map((item) => <TodoItem item={item} deleteTodo={deleteTodo} />)}
        </table>
        <Link to='/todos/create'>Create</Link>
        </div>
    )
}
export default TodoList