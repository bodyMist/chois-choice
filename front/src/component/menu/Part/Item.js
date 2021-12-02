import styled from "styled-components";
import { Link, Route, Switch } from "react-router-dom";
const MainInfo = styled.div`
positon: relative;
width: 100%;
display: table;
border-bottom: 1px solid #b3b3b3;
`
const Name = styled(Link)`
display : inline;
font-weight: bold;
color: #000;
line-height: 22px;
margin-right: 6px;
vertical-align: middle;
`
const Thumb = styled.div`
display: table-cell;
width: 150px;
vertical-align: top;
`
const ThumbLink = styled.a`
display: inline-block;
position: relative;
width: 130px;
height: 130px;
`
const IMG = styled.img`
vertical-align:top;
width:130px;
max-width:100%;
max-height:100%;
`
export default function Item({list}) {
 
  return(
    <li>
      <MainInfo>
        <Thumb>
          <ThumbLink>
            <IMG src={list.component_component.image_url} />
          </ThumbLink>
        </Thumb>
        <Name id={list.component_component.component_id} 
        to={{
          pathname:`/ComponentDetail`,
          data: list
        }}>
          {list.component_component.name}
        </Name>
      </MainInfo>
    </li>
  );
}