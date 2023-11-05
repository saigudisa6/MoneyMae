import './quote.css';

function Quote(){
    const quoteText = "\"A housing innovator that helps people\"";

    return(
        <div className='quote-container'>
            <div className='quote'><b>{quoteText}</b></div>
        </div>
    )
}

export default Quote;