export default function BestPost() {
    return (
        <div className="articleList">
            <ul className="list">
                <li className="articleSubject">
                    <a className="subject" href="#">
                        <span className="title">
                            <strong>부품추천 1</strong>
                        </span>
                    </a>
                    <span className="info">
                        <em className="writer">작성자</em>
                        &nbsp;|&nbsp;
                        {/* <span>조회:1</span>
                        &nbsp;&nbsp;|&nbsp; */}
                        <span>02:59</span>
                    </span>
                </li>
                <li className="articleSubject">
                    <a className="subject" href="#">
                        <span className="title">
                            <strong>부품추천 2</strong>
                        </span>
                    </a>
                    <span className="info">
                        <em className="writer">작성자</em>
                        &nbsp;|&nbsp;
                        {/* <span>조회:1</span>
                        &nbsp;&nbsp;|&nbsp; */}
                        <span>02:59</span>
                    </span>
                </li>
            </ul>
        </div>
    );
}
