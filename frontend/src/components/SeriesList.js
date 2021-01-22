import React, { Component } from 'react';

function SeriesList({ allSeries }) {
  return (
    <ul className='SeriesList'>
      {allSeries.map(series => (
        <SeriesItem key = {series.id} series={series} />
      ))}
    </ul>
  )
}

function SeriesItem({ allSeries }) {
  return(
    <li>
      
        <a href='../pages/SingleSeriesPage'>
          {series.title}
        </a>
      
    </li>
  )
}

export default SeriesList;