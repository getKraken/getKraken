import React from 'react';

class SingleSeriesForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
        eventList : [],
        participantList : [],
    }
  }
  componentDidMount(){
    // GET the API for the Events List
    this.setState({
      eventList : [
        {
            "id": 4,
            "series": 3,
            "description": "event1",
            "host": null
        },
        {
            "id": 5,
            "series": 3,
            "description": "event2",
            "host": null
        }
    ]
    })

    // fetch(base + '/api/v1/event')
    //   .then(res => res.json())
    //     .then(result => this.setState({
    //       eventList : result
    //     }))

    //Get data from the series list
  }
  render(){
    return(
      <>
        <ul>
          {this.state.eventList.map(event => (
            <li>
              {event.description}
            </li>
          ))}  
        </ul>
      </>
    )
  }
}

export default SingleSeriesForm