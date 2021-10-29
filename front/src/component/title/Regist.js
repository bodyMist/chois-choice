import { Link } from "react-router-dom";

export default function Regist() {
    return (
        <div className="regist-form">
            <h2>회원가입</h2>
            <input type="text" name="email" className="text-field" placeholder="ID"/>
            <input type="password" name="password" className="text-field" placeholder="PASSWORD"/>
            <input type="password" name="repeat-password" className="text-field" placeholder="REPEAT PASSWORD"/>
            <input type="submit" className="submit-btn"/>
            <h4>
                <Link to="/">돌아가기</Link>
            </h4>
        </div>
    );
}