import { Link } from "react-router-dom";

export default function Login() {
    
    return (
        <div className="login-form">
            <h2>Login</h2>
            <input type="text" name="email" className="text-field" placeholder="ID"/>
            <input type="password" name="password" className="text-field" placeholder="PASSWORD"/>
            <input type="submit" value="로그인" className="submit-btn"/>

            <h4>
                <Link to="/">돌아가기</Link>
            </h4>
        </div>
    );
}