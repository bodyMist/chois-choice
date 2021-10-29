import { Link } from "react-router-dom";

export default function PcRecommand() {
    return (
        <div className="container">
            {/* <h3>PC 견적 추천</h3> */}
            <Link to="/Estimate">견적 작성</Link>
            <div className="input-group-pc">
                <input
                    type="text"
                    className="form-control"
                    placeholder="예산 입력"
                ></input>
                <input
                    type="text"
                    className="form-control second"
                    placeholder="용도 입력"
                ></input>
                <button className="btn btn-default">제출</button>
            </div>
            <div className="text-center">
                <h5>결과</h5>
                <span></span>
            </div>
        </div>
    );
}
