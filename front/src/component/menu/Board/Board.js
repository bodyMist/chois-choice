import Post from "./Post"

export default function Board () {
  return (
    <div className="articleList">
      <ul className="list">
        {/* 서버에서 게시글 가져온걸로 li 만들어서 게시판 작성하면 됨 */}
        <Post/>
      </ul>
    </div>
  );
}