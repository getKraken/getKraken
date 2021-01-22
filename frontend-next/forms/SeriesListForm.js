import React from 'react';

class SeriesListForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      seriesList : [],
    }
  }
  componentDidMount(){
    this.setState({
      seriesList: []
    //   seriesList: [
    //     {
    //       "id" : 1,
    //       "title": "2021-kraken",
    //       "organizer": 'yoni',
    //       "participants": [
    //         1,
    //         2
    //       ]
    //     },
    //     {
    //       "id" : 2,
    //       "title": "2021-kraken",
    //       "organizer": 'yoni',
    //       "participants": [
    //         1,
    //         2
    //       ]
    //     },
    //     {
    //       "id" : 3,
    //       "title": "2021-kraken",
    //       "organizer": 'yoni',
    //       "participants": [
    //         1,
    //         2
    //       ]
    //     }
    //   ],
    })
    
    fetch('http://get-kraken.herokuapp.com/api/v1/series/')
      .then(res => res.json())
        .then(result => this.setState({
          [seriesList] : [result]
        }))
  }
  render(){
    return(
      <ul>
        {this.state.seriesList.map(series => (
            <li>        
              {series.title}
              {series.id}      
            </li>
        ))}
      </ul>
    )
  }
}

export default SeriesListForm;