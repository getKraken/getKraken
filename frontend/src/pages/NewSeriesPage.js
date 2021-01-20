import React from 'react';
import NavBar from '../components/NavBar'
import NewSeriesForm from '../components/NewSeriesForm'
import NewEventForm from '../components/NewEventForm'

class NewSeriesPage extends React.Component {
  render(){
    return (
      <div className="NewSeriesPage">
        <NavBar></NavBar>
        <NewSeriesForm>
          <NewEventForm></NewEventForm>
        </NewSeriesForm>
      </div>
    );
  }

}

export default NewSeriesPage;