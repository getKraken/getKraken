import React from 'react';
import SubmitButton from '../components/SubmitButton';
import Router from 'next/router';
import Link from 'next/link';

class SeriesListForm extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            disableButton: false
        }
    }

    render() {
        return (
            <>
            <div>

                {this.props.seriesData.length ?
                    <ul>
                        {this.props.seriesData.map(series => (
                            <li key={series.id}>
                                <Link href="/series/[id].js" as={`/series/${series.id}`}>
                                    <a>{series.title}</a>
                                </Link>
                            </li>
                        ))}
                    </ul>

                    : <h2>create something!</h2>}
            </div>
            </>
        )
    }
}

export default SeriesListForm;

/*
           <>
            	<div className="container mx-auto flex flex-col md:flex-row items-center my-12 md:my-24">

		<div className="flex flex-col w-full lg:w-1/2 justify-center items-start pt-12 pb-24 px-6">
			<p className="uppercase tracking-loose">Witty Tagline</p>
			<h1 className="my-4">All of my Series'</h1>
			<p className="leading-normal mb-4">Enter your super app's description here... The key is to find the right length.  Don't want it to be too long, but then don't want it to be too short so that it looks weird between the title and button below.</p>
			<button className="bg-transparent hover:bg-black text-black hover:text-white rounded shadow hover:shadow-lg py-2 px-4 border border-black hover:border-transparent">Super Button</button>
		</div>

		<div className="w-full lg:w-1/2 lg:py-6 text-center">

			<svg className="fill-current text-black w-3/5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20"><path d="M17 6V5h-2V2H3v14h5v4h3.25H11a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6zm-5.75 14H3a2 2 0 0 1-2-2V2c0-1.1.9-2 2-2h12a2 2 0 0 1 2 2v4a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-5.75zM11 8v8h6V8h-6zm3 11a1 1 0 1 0 0-2 1 1 0 0 0 0 2z"/></svg>
		</div>

	  </div> */
