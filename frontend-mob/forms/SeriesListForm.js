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
    routerseries(seriesId) {
        Router.push(`../pages/single-series/${seriesId}`)
    }

    render() {
        return (
            <>
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

                    : <h1>create something</h1>}
            </>
        )
    }
}

export default SeriesListForm;
