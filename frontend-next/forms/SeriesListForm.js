import React from 'react';
import SubmitButton from '../components/SubmitButton';
import Router from 'next/router';
class SeriesListForm extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
      seriesList: [],
      disableButton: false
    }
  }
  routerseries(seriesId) {
    Router.push(`../pages/single-series/${seriesId}`)
  }
  componentDidMount() {

    fetch('http://get-kraken.herokuapp.com/api/v1/series')
      .then(res => res.json())
      .then(result => {
        if (result.length != 0) {
          this.setState({
            seriesList: result,
            disableButton :true
          })
        }
      })
  }
  render() {
    return (
      <>
        {this.state.seriesList.length ?
          <ul>
            {this.state.seriesList.map(series => (
              <li>
                <SubmitButton
                  text = {series.title}
                  disabled = {this.state.disableButton}
                  onClick ={()=>this.routerseries(`${series.id}`)}
                />
              </li>
            ))}
          </ul>

          : <h1>create something</h1>}
      </>
    )
  }
}

export default SeriesListForm;