import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import axios from 'axios';
import UserList from './components/User.js'
import ProjectList from './components/Project.js'
import TodoList from './components/Todo.js'
import UserProjectList from './components/UserProject.js'
import LoginForm from './components/Auth.js'
import ProjectForm from './components/ProjectForm.js'
import TodoForm from './components/TodoForm.js'
import {HashRouter, Route, Link, Switch, Redirect, BrowserRouter} from 'react-router-dom'
import Cookies from 'universal-cookie'


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

        this.state = {
        'users': [],
        'projects': [],
        'todos': [],
        }
    }

    set_token(token) {
        const cookies = new Cookies()
        cookies.set('token', token)
        // localStorage.setItem('token', token)
        this.setState({'token': token}, ()=>this.load_data())
    }

    is_authenticated() {
        return this.state.token != ''
    }

    logout() {
        this.set_token('')
    }

    get_token_from_storage() {
        const cookies = new Cookies()
        const token = cookies.get('token')
        this.setState({'token': token}, ()=>this.load_data())
    }

    get_token(login, password) {
        axios.post('http://127.0.0.1:8000/api-token-auth/', {username: login, password: password})
        .then(response => {
            this.set_token(response.data['token'])
        }).catch(error => alert('Неверный логин или пароль'))
}

    get_headers() {
        let headers = {
            'Content-Type': 'application/json'
        }
        if (this.is_authenticated()) {
            headers['Authorization'] = 'Token ' + this.state.token
        }
        return headers
    }


    createProject(name, repo_link, user) {
        const headers = this.get_headers()
        const data = {name: name, repo_link: repo_link, user: user}
        axios.post('http://127.0.0.1:8000/api/projects/', data, {headers})
            .then(response => {
                let new_project = response.data
                new_project.name = ''
                new_project.repo_link = ''
                const user = this.state.users.filter((user) => user.id === new_project.user)[0]
                new_project.user = user
                this.setState({projects: [...this.state.projects, new_project]})
            }).catch(error => console.log(error))
    }


    createTodo(project, text, user, is_active) {
        const headers = this.get_headers()
        const data = {project: project, text: text, user: user, is_active: is_active}
        axios.post('http://127.0.0.1:8000/api/todos/', data, {headers})
            .then(response => {
                let new_todo = response.data
                const project = this.state.projects.filter((item) => item.id === new_todo.project)[0]
                new_todo.project = project
                new_todo.text = ''
                const user = this.state.users.filter((user) => user.id === new_todo.user)[0]
                new_todo.user = user
                new_todo.is_active = true
                this.setState({todos: [...this.state.todos, new_todo]})
            }).catch(error => console.log(error))
    }



    deleteProject(id) {
        const headers = this.get_headers()
        axios.delete('http://127.0.0.1:8000/api/projects/${id}', id, {headers})
            .then(response => {this.setState({projects: this.state.projects.filter((item)=>item.id !== id)})
            }).catch(error => console.log(error))
    }


    deleteTodo(id) {
        const headers = this.get_headers()
        axios.delete('http://127.0.0.1:8000/api/todos/${id}', {headers})
            .then(response => {
                this.setState({todos: this.state.todos.filter((item)=>item.id !== id)})
            }).catch(error => console.log(error))
    }


    load_data() {
        const headers = this.get_headers()
        axios.get('http://127.0.0.1:8000/api/users/', {headers})
            .then(response => {
                const users = response.data
                this.setState({'users': users})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/projects/', {headers})
            .then(response => {
                const projects = response.data
                this.setState({'projects': projects})
            }).catch(error => console.log(error))

        axios.get('http://127.0.0.1:8000/api/todos/', {headers})
            .then(response => {
                const todos = response.data
                this.setState({'todos': todos})
            }).catch(error => console.log(error))
    }

    componentDidMount() {
        this.get_token_from_storage()
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
                            <li>
                                {this.is_authenticated() ? <button onClick={()=>this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}

                            </li>
                        </ul>
                    </nav>
                    <Switch>
                        <Route exact path='/' component={() => <UserList users={this.state.users} /> }/>
                        <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} /> }/>
                        <Route exact path='/todos' component={() => <TodoList items={this.state.todos} /> }/>
                        <Route exact path='/login' component={() => <LoginForm get_token={(login, password) => this.get_token(login, password)} />} />
                        <Route exact path='user/:id' component={() => <UserProjectList items={this.state.project} /> }/>
                        <Route exact path='/projects/create' component={() => <ProjectForm users={this.state.users} createProject={(name, repo_link, user) => this.createProject(name, repo_link, user)} />} />
                        <Route exact path='/projects' component={() => <ProjectList items={this.state.projects} deleteProject={(id)=>this.deleteProject(id)} />} />
                        <Route exact path='/todos/create' component={() => <TodoForm projects={this.state.projects} users={this.state.users} createTodo={(project, text, user, is_active) => this.createTodo(project, text, user, is_active)} />} />
                        <Route exact path='/todos' component={() => <TodoList items={this.state.todos} deleteTodo={(id)=>this.deleteTodo(id)} />} />

                        <Redirect from='/users' to='/' />
                        <Route component={NotFound404}/>
                    </Switch>
                </BrowserRouter>

            </div>

        )
    }
}
export default App;
