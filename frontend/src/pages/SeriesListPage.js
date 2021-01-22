import React from 'react';
import SingleSeries from '../components/SeriesList';
import NavBar from '../components/NavBar';
import SubmitButton from '../components/SubmitButton';

class SeriesListPage extends React.Component {
  render(){
    return (
      <div className="SeriesListPage">
          <NavBar></NavBar>
          <p>Welcome Username!</p>

          <h2>Current Series</h2>
          <ol>
              <li>Current Series #1</li>
              <li>Current Series #2</li>
              <li>Current Series #3</li>
          </ol>
          <h2>Past Series</h2>
          <ol>
            <li>Past Series #1</li>
            <li>Past Series #2</li>
            <li>Past Series #3</li>
          </ol>
      </div>
    );
  }

}

export default SeriesListPage;