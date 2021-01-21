import React from 'react';
import SubmitButton from '../components/SubmitButton'

class NewSeriesForm extends React.Component {
  render(){
    return (
      <div className="newSeriesForm">
        <form>
            <label for='series-title'>Series Title:</label>
            <input type='text' id='series-title'></input>
            <label for='series-description'>Series Description:</label>
            <input type='text' id='series-description'></input>
            <SubmitButton>Create New Series</SubmitButton>
        </form>
      </div>
    );
  }

}

export default NewSeriesForm;