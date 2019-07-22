import React, { Component } from 'react';
import './App.css';


// create a list variable 

const list = [
  {
    'id': 1,
    'title': '1st Item',
    'description': '1st Item 1st Item 1st Item 1st Item '
  },
  {
    'id': 1,
    'title': '1st Item',
    'description': '1st Item 1st Item 1st Item 1st Item '
  }
]

class App extends Component {
  // now creating a state in which our data from DRF will save
  state = {
    todos: []
  };

  // connecting DRF to React Async
  async componentDidMount() {
    try{
      const con = await fetch('http://127.0.0.1:8000/data/');
      const todos = await con.json();

      this.setState({
        todos
      });
    } 
    catch (e) {
      console.log(e);
    }
  }
  // end connection to json data from DRF



  render(){
    return(
      <div className="App">
        <h1>Happy Django React</h1>
        {this.state.todos.map(item => (
          <div>
            <h2>{item.title}</h2>
            <p>{item.description}</p>
          </div>
        ))}
      </div>


    );
  }
}

export default App;
