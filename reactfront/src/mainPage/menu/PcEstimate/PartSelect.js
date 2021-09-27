export default function PartSelect() {
    return (
        <div className="col-xs-12 container-partSelect">
            <div className="col-xs-12 parts">
                <div className="col-xs-1 col-xs-2 searchInputArea">
                    <div className="input-group">
                        <input type="text" className="form-control" placeholder="부품 명 검색"></input>
                        <div className="input-group-btn">
                            <button className="btn btn-default" type="button">검색</button>
                            <button className="btn btn-default" type="button">초기화</button>
                        </div>
                   </div>
               </div>
               <div className="StuffListView">
                   <div className="StuffList">
                       <div className="StuffIcon">
                            <img alt="1" src="/1.jpg"/>
                       </div>
                       <div className="btn text-left">
                            <span>CPU : </span>
                            <span className="label label-info">추천</span>
                            <span>AMD 3600 (정품)</span>
                       </div>
                   </div>
                   <div className="StuffList">
                       <div className="StuffIcon">
                            <img alt="1" src="/1.jpg"/>
                       </div>
                       <div className="btn text-left">
                            <span>CPU : </span>
                            <span className="label label-info">추천</span>
                            <span>AMD 3600 (정품)</span>
                       </div>
                   </div><div className="StuffList">
                       <div className="StuffIcon">
                            <img alt="1" src="/1.jpg"/>
                       </div>
                       <div className="btn text-left">
                            <span>CPU : </span>
                            <span className="label label-info">추천</span>
                            <span>AMD 3600 (정품)</span>
                       </div>
                   </div><div className="StuffList">
                       <div className="StuffIcon">
                            <img alt="1" src="/1.jpg"/>
                       </div>
                       <div className="btn text-left">
                            <span>CPU : </span>
                            <span className="label label-info">추천</span>
                            <span>AMD 3600 (정품)</span>
                       </div>
                   </div><div className="StuffList">
                       <div className="StuffIcon">
                            <img alt="1" src="/1.jpg"/>
                       </div>
                       <div className="btn text-left">
                            <span>CPU : </span>
                            <span className="label label-info">추천</span>
                            <span>AMD 3600 (정품)</span>
                       </div>
                   </div>
               </div>
            </div>
        </div>
    );
}