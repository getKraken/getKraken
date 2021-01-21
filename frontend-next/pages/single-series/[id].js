export default function SeriesDetail(){
  oneSeries = {id:1,title:'kraken2021',description:'hockey team in seattle, season tickets', members: ['mark','yoni','will','paul']}
  return(
    <div className='SingleSeriesPage'>
      <div id='seriesDetails'>
        <h2>{oneSeries.title}</h2>
        <p>{oneSeries.description}</p>
        <p>{oneSeries.members}</p>
      </div>
    </div>
  )
}

