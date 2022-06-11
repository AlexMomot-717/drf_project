import React from 'react'


class TodoForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {project: props.project[0].id, text: '', user: props.user[0].id, is_active: true}
    }

    handleChange(event) {
        this.setState(
            {
                [event.target.name]: event.target.value
            }
        );
    }

    handleSubmit(event) {
        this.props.createTodo(this.state.project, this.state.text, this.state.user, this.state.is_active)
        event.preventDefault()
    }

    render() {
        return (
            <form onSubmit={(event)=> this.handleSubmit(event)}>
                <div className="form-group">
                    <label for="project">project</label>
                        <select name="project" className='form-control' onChange={(event)=>this.handleChange(event)}> {this.props.projects.map((item)=><option value={item.id}>{item.name}</option>)}
                        </select>
                </div>

                <div className="form-group">
                    <label for="text">text</label>
                        <input type="text" className="form-control" name="text"
                        value={this.state.text} onChange={(event)=>this.handleChange(event)} />

                </div>

                <div className="form-group">
                    <label for="user">user</label>
                        <select name="user" className='form-control' onChange={(event)=>this.handleChange(event)}> {this.props.users.map((user)=><option value={user.id}>{user.name}</option>)}
                        </select>

                </div>

                <div className="form-group">
                    <label for="is_active">is_active</label>
                        <input type="boolean" className="form-control" name="is_active"
                        value={this.state.is_active} onChange={(event)=>this.handleChange(event)} />

                </div>

                <input type="submit" className="btn btn-primary" value="Save" />
            </form>
        );
    }
}


export default TodoForm