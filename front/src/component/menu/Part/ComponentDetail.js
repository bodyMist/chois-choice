export default function ComponentDetail({location}) {
  const list = Object.entries(location);

  return (
      <div>
          <li className="Part-list">
              {/* <div className="PartName">
                  <strong>{location.data.component_component.name}</strong>
              </div>
              <div className="PartItem">
                  <div className="Part-image">
                      <img src={location.data.component_component.image_url} />
                  </div>
                  <div className="Part-inf-box">
                      <span className="Part-inf">
                          {location.data.generation}
                      </span>
                  </div>
                  <div className="Part-inf-box">
                      <span className="Part-inf">
                          {location.data.max_clock}
                      </span>
                  </div>
                  <div className="Part-inf-box">
                      <span className="Part-inf">
                          {location.data.socket}
                      </span>
                  </div>
                  <div className="Part-inf-box">
                      <span className="Part-inf">
                          {location.data.tdp}
                      </span>
                  </div>
                  <div className="Part-inf-box">
                      <span className="Part-inf">
                          {location.data.thickness}
                      </span>
                  </div>
              </div> */}
            {list.map((item, index)=>{
              if(index == 1) {

              }
            })}
          </li>
      </div>
  );
}