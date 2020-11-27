import React, {Component} from 'react';
import PropTypes from 'prop-types';
import _ from "lodash";
import RGL, { WidthProvider } from "react-grid-layout";
import "../assets/dragdash.css"

const ReactGridLayout = WidthProvider(RGL);
/**
 * GridComponent is an dash component.
 * It takes a property, `id`, and children to
 * displays it.
 */
export default class DashGrid extends Component {

      constructor(props) {
        super(props);

        const layout = this.props.position;
        this.state = { 
           layout,
          // data
           };
        this.onAddItem = this.onAddItem.bind(this);
        this.onBreakpointChange = this.onBreakpointChange.bind(this);
        this.onLayoutChange = this.onLayoutChange.bind(this);
      }

      componentWillMount() {
        this.setState({ layout : this.props.position }); 
        if(this.props.editable)
        {
          console.log(this.props.editable,"edit now")
          this.props.setProps({ isDraggable : true ,isResizable : true });
        }
        else{
          this.props.setProps({ isDraggable : false ,isResizable : false });
        }
      }

      generateLayout() {
        const p = this.props;
        //console.log("count",React.Children.count(this.props.children))
        return _.map((this.props.children), function(item, i) {
          const y = _.result(p, "y") || Math.ceil(Math.random() * 4) + 1;
          //console.log("p",p)
          //console.log("item",item)
          return {
            x: (i * 2) % 12,
            y: Math.floor(i / 6) * y,
            w: 2,
            h: y,
            i: item.key.toString()
          };
        });
      }

    onLayoutChange(layout) {
      //console.log("layout",layout)
      //saveToLS("layout", layout);
      this.setState({ layout : layout });
      this.props.setProps({ position: this.state.layout })
      //this.props.onLayoutChange(layout);
    }

    setPositiononLoad( ){
        this.setState({ layout : this.props.position });
    }

    stringifyLayout() {
      //console.log("stringify",this.state.layout)
      return this.state.layout.map(function(l) {
        const name = l.i === "__dropping-elem__" ? "drop" : l.i;
        return (
          <div className="layoutItem" key={l.i}>
            <b>{name}</b>
            {`: [${l.x}, ${l.y}, ${l.w}, ${l.h}]`}
          </div>
        );
      });
    }

    onAddItem() {
    /*eslint no-console: 0*/
      console.log("adding", "n" + this.state.newCounter);
      this.setState({
        // Add a new item. It must have a unique key!
        layout: this.state.layout.concat({
          i: "n" + this.state.newCounter,
          x: (this.state.layout.length * 2) % (this.state.cols || 12),
          y: Infinity, // puts it at the bottom
          w: 2,
          h: 2
        }),
        // Increment the counter to ensure key is always unique.
        newCounter: this.state.newCounter + 1
      });
    }
      onBreakpointChange(breakpoint, cols) {
        this.setState({
          breakpoint: breakpoint,
          cols: cols
        });
      }

    render() {
        const {id, children, position, setProps , editable } = this.props;
        
        let myAttr = {'grid-position': JSON.stringify(this.state.layout) }
        return (
            <div id={id} {...myAttr}  >
                    <ReactGridLayout
                        {...this.props}
                        layout={this.state.layout}
                        onBreakpointChange={this.onBreakpointChange}
                        onLayoutChange={this.onLayoutChange}     
                      >
                      {this.props.children.map((child, index) => (<div key={child.key}>{child}</div>))}
                    </ReactGridLayout>
            </div>
        );
    }
}


DashGrid.defaultProps = {
    className: "layout",
    items: 50,
    cols: 12,
    rowHeight: 30,
    // This turns off compaction so you can place items wherever.
    verticalCompact: false,
    isDraggable : false,
    isResizable : false,
    // This turns off rearrangement so items will not be pushed arround.
    preventCollision: true
};

DashGrid.propTypes = {
    /**
     * The ID used to identify this component in Dash callbacks.
     */
    id: PropTypes.string,

    /**
     * The children components displayed inside the grid.
     */
    children : PropTypes.node,

    editable :PropTypes.bool,

    /**
     * The layout of the  components displayed inside the grid.
     */
    position : PropTypes.array,
    
    /**
     * Dash-assigned callback that should be called to report property changes
     * to Dash, to make them available for callbacks.
     */
    setProps: PropTypes.func
};
