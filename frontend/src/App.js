import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TodoList from './components/Todo.js'
import UserProjectList from './components/UserProject.js'
import {HashRouter, Route, Link, Switch, Redirect, BrowserRouter} from 'react-router-dom'


const NotFound404 = ({ location }) => {
    return (
        <div>
            <h1>Страница по адресу '{location.pathname}' не найдена</h1>
        </div>
    )
}
class App extends React.Component {
    constructor(props) {
        super(props)

        const user1 = {id: 1, username: 'user1', first_name: 'Иван', last_name: 'Иванов', email: 'iv@mail.ru'}
        const user2 = {id: 2, username: 'user2', first_name: 'Петр', last_name: 'Петров', email: 'petr@mail.ru'}
        const user3 = {id: 3, username: 'user3', first_name: 'Борис', last_name: 'Борисов', email: 'boris@mail.ru'}
        const users = [user1, user2, user3]

        const project1 = {id: 1, name: 'project1', repo_link: 'http//some_repo_link1', user: user1}
        const project2 = {id: 2, name: 'project2', repo_link: 'http//some_repo_link2', user: user3}
        const project3 = {id: 3, name: 'project3', repo_link: 'http//some_repo_link3', user: user2}
        const projects = [project1, project2, project3]

        const todo1 = {project_id: 1, text: 'написать тесты', created_at: '10.03.2022', updated_at: '10.03.2022', user: user1, is_active: 'True'}
        const todo2 = {project_id: 3, text: 'добавить статус заказа в ЛК', created_at: '27.04.2022', updated_at: '11.05.2022', user: user3, is_active: 'True'}
        const todo3 = {project_id: 2, text: 'добавить оплату картой в ЛК', created_at: '20.04.2022', updated_at: '11.05.2022', user: user2, is_active: 'True'}
        const todos = [todo1, todo2, todo3]

        this.state = {
        'users': users,
        'projects': projects,
        'todos': todos,
        }
    }


    render () {
        return (
            <div className='App'>
                <BrowserRouter>
                    <nav>
                        <ul>
                            <li>
                                <Link to='/'>Users</Link>
                            </li>
                            <li>
                                <Link to='/projects'>Projects</Link>
                            </li>
                            <li>
                                <Link to='/todos'>Todos</Link>
                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users} /> }/>
                        <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} /> }/>
                        <Route exact path='/todos' component={() => <TodoList items={this.state.todos} /> }/>
                        <Route exact path='user/:id' component={() => <UserProjectList items={this.state.projects} /> }/>
                        <Redirect from='/users' to='/' />
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>

            </div>

        )
    }
}
export default App;
