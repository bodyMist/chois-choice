import { Link } from "react-router-dom";

export default function Header() {
    return (
        <div className="header">
            <h1>
                <Link to="/">Choi's Choice</Link>
            </h1>
            <div className="menu">
                {/* <Link className="link" to="/Login">로그인</Link>
                <Link className="link" to="/Regist"> 회원가입</Link> */}
            </div>
        </div>
    );
}