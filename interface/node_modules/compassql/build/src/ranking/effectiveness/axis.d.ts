/**
 * Field Type (with Bin and TimeUnit) and Channel Score (Cleveland / Mackinlay based)
 */
import { Channel } from 'vega-lite/build/src/channel';
import { QueryConfig } from '../../config';
import { SpecQueryModel } from '../../model';
import { Schema } from '../../schema';
import { Dict } from '../../util';
import { FeatureScore } from '../ranking';
import { Scorer } from './base';
import { ExtendedType } from './type';
/**
 * Effectiveness Score for preferred axis.
 */
export declare class AxisScorer extends Scorer {
    constructor();
    protected initScore(opt?: QueryConfig): Dict<number>;
    featurize(type: ExtendedType, channel: Channel): string;
    getScore(specM: SpecQueryModel, _: Schema, __: QueryConfig): FeatureScore[];
}
