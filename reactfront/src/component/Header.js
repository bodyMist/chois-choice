import { Link } from "react-router-dom";

export default function Header() {
    return (
        <div className="header">
            <h1>
                <Link to="/">Choi's Choice</Link>
            </h1>
            <div className="menu">
                <a href="#x" className="link">
                    로그인
                </a>
                <a href="#x" className="link">
                    회원가입
                </a>
            </div>
        </div>
    );
}